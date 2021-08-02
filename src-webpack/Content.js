import React, { Component} from "react";
import Container from "react-bootstrap/Container";
import Spinner from "react-bootstrap/Spinner";
import Post from "./Post.js"
import ContentPagination from "./ContentPagination.js";
import ContentComments from "./ContentComments.js";
import "./css/Content.css"

class Content extends Component
{
	constructor (props)
	{
		super(props);
	}
	
	render ()
	{
		return(
			<Container fluid className="ContentContainer">
				{   this.props && this.props.posts &&
					this.props.posts.map((postData) => {
					  return <Post key={postData.id} postData={postData} />
					})
				|| (
					<Spinner animation="border" role="status" variant="secondary">
					  <span className="visually-hidden">Loading...</span>
					</Spinner>
					)
				}

				{ this.props.comments &&
					<ContentComments comments={this.props.comments}/>
				}

				{ this.props.pagination &&
					<ContentPagination pagination={this.props.pagination}/>
				}
			</Container>
		);
	}
}

export default Content;