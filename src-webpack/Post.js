import React, { Component} from "react";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import PostImage from "./PostImage.js"
import PostUnknown from "./PostUnknown.js"
import "./css/Post.css";

class Post extends Component
{
  render ()
  {
    return(
		<Container fluid className="PostWrapper bg-dark border border-dark rounded">
			<Row>
				<Col>{ this.renderPost(this.props.postData) }</Col>
			</Row>
		</Container>
    );
  }
  
  renderPost(postData = null)
  {
	  switch(postData.type)
	  {
		  case ('image-regular'):
			return this.renderPostImage(postData);
	  }
	  
	  return (this.renderPostUnknown(postData));
  }
  
  renderPostImage(postData)
  {
	  return (
		<PostImage postData={postData} />
	  );
  }
  
  renderPostUnknown (postData)
  {
	  return (
		<PostUnknown postData={postData} />
	  );
  }
}

export default Post;
