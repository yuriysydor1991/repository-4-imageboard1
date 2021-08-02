import React, { Component} from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Header from "./Header.js";
import Content from "./Content.js";
import Footer from "./Footer.js";
import ServerResponse from "./ServerResponse.js";
import "./css/App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

class App extends Component
{
  constructor(props)
  {
	  super(props);
	  
	  this.state = {
		  posts: props.posts,
		  pagination: props.pagination
	  };
  }
  
  render ()
  {	
    return (
      <Container>
        <Header></Header>
		<Content posts={this.state.posts} pagination={this.state.pagination}></Content>
		<Footer></Footer>
      </Container>
    ) ;
  }
  
  componentDidMount () 
  {
    fetch("/rest/v1/general/home_content" + window.location.search)
      .then(res => res.json())
      .then(
        (result) => {
		  console.log("Fetched server result:");
		  console.log(result);
		  
		  let checker = new ServerResponse();
		  
		  if (checker.check(result))
		  {
			  if (result.content.hasOwnProperty('posts'))
				  this.setState({
					posts: result.content.posts.list,
				  });
			  
			  if (result.content.hasOwnProperty('pagination'))
				this.setState({
					pagination: result.content.pagination
				})
		  }
		  else
			  console.log ('Unrecognized server response!');
        },
        // Примітка: важливо обробляти помилки саме тут,
        // а не в блоці catch (), щоб не перехоплювати
        // виключення з помилок в самих компонентах.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }
}

export default App;
