import React, { Component} from "react";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faLink } from '@fortawesome/free-solid-svg-icons'
import { faEye } from '@fortawesome/free-solid-svg-icons'
import { faCalendarAlt } from '@fortawesome/free-solid-svg-icons'
import { faCommentAlt } from '@fortawesome/free-solid-svg-icons'
import "./css/PostImage.css";

class PostImage extends Component
{
  render ()
  {
    return(
		<Container fluid>
		
			<div>
				<a className="text text-success" href={this.props.postData.url}>
					<h2 className="postTitle text-light">
					{this.props.postData.title}
					</h2>{' '}
				</a>
			</div>
			
			<Row className="postImageWrapper">
				<a className="text text-success" href={this.props.postData.url}>
					<Image src={this.props.postData.img} 
						 alt={this.props.postData.title}
						 title={this.props.postData.title}
						 className="postImage"
						 fluid
					/>
				</a>
			</Row>
			
			<div className="postTools">
				<Button variant="secondary">
					<FontAwesomeIcon icon={faCalendarAlt} />{' '}
					{this.props.postData.date}
				</Button>{' '}
				<Button variant="secondary">
					<FontAwesomeIcon icon={faEye} />{' '}
					{this.props.postData.views}
				</Button>{' '}
				<a href={this.props.postData.url} className="btn btn-secondary">
					<FontAwesomeIcon icon={faCommentAlt} />{' '}
					{this.props.postData.comments}
				</a>
			</div>
			
		</Container>
    );
  }
}

export default PostImage;
