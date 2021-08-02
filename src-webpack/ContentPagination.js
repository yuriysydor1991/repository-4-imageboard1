import React, { Component} from "react";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";
import './css/ContentPagination.css';

class ContentPagination extends Component
{
	render ()
	{
		return(
			<Container fluid className="ContentPagination">
				{ this.props && this.props.pagination &&
						this.props.pagination.map((pagination, index) => {
							return (
								<Button	key={index} 
										className="PaginationButton btn-lg" 
										variant="dark"
										href={pagination.link}
								>
									{pagination.title}
								</Button>
							);
						})
				}
			</Container>
		);
	}
}

export default ContentPagination;