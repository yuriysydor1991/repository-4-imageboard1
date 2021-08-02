import React, { Component} from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Header from "./Header.js";
import Content from "./Content.js";
import Footer from "./Footer.js";
import ServerResponse from "./ServerResponse.js";
import "./css/AppPost.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

class AppPost extends Component
{
  constructor(props)
  {
	  super(props);
	  
	  this.state = {
		  posts: props.posts,
		  pagination: props.pagination,
		  comments: props.comments
	  };
  }
  
  render ()
  {	
    return (
      <Container>
        <Header />
		<Content	posts={this.state.posts} 
					pagination={this.state.pagination} 
					comments={this.state.comments}
		/>
		<Footer />
      </Container>
    ) ;
  }
  
  componentDidMount () 
  {
	let matches = location.href.match(/\/post\/(?<postUrl>[^\/\?]+)/)
	let postUrl = '?unknown_url=yes';
	
	if (matches != null)
		postUrl = '?post_url=' + matches[1];
	
    fetch("/rest/v1/general/post_content" + postUrl)
      .then(res => res.json())
      .then(
        (result) => {
		  console.log("Fetched server result 4 post content:");
		  console.log(result);
		  
		  let checker = new ServerResponse();
		  
		  if (checker.check(result))
		  {
			  this.setState({
				posts: result.content.posts.list
			  });
		  }
		  else
			  console.log ('Unrecognized server response!');
        },
        (error) => {
			console.log(error)
        }
      )

	fetch("/rest/v1/general/post_comments" + postUrl)
      .then(res => res.json())
      .then(
        (result) => {
		  console.log("Fetched server result 4 post comments:");
		  console.log(result);
		  
		  let checker = new ServerResponse();
		  
		  if (checker.check(result))
		  {
			  this.setState({
				comments: result.content
			  });
		  }
		  else
			  console.log ('Unrecognized server response!');
        },
        (error) => {
			console.log(error)
        }
      )
  }
}

export default AppPost;
