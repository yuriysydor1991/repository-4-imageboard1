import React, { Component} from "react";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";
import Button from "react-bootstrap/Button";
import Alert from "react-bootstrap/Alert";
import Form from "react-bootstrap/Form";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser } from '@fortawesome/free-solid-svg-icons'
import "./css/ContentComments.css"

class ContentComments extends Component
{
  render ()
  {
	  if (!this.props.comments || this.props.comments == null || this.props.comments.length == 0)
		return (null);
	
    return(
		<Container fluid className="ContentComments bg-dark border border-dark rounded">
				<Form.Label className="text-muted">All the comments</Form.Label>
				<div>
					{ this.props.comments.map((commentData, key) => {
						  return (
							<Alert key={key} variant="dark" className="ContentCommentAlert">
								<Alert.Heading>
									{ commentData.user_logo && 
										(<img class="commentUserLogo" src={commentData.user_logo}/>)
									|| (<FontAwesomeIcon icon={faUser} />)
									}
									{' '}{ commentData.user_nickname }{' '}
									<Form.Label className="text-muted">({ commentData.user_email })</Form.Label>{' '}
									<Form.Label>at { commentData.date }</Form.Label>
								</Alert.Heading>
								<p>
									{ commentData.comment }
								</p>
							</Alert>
						  );
						})
					}
				</div>
		</Container>
    );
  }
}

export default ContentComments;
