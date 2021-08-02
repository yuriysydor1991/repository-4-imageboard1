import React, { Component} from "react";
import Container from "react-bootstrap/Container";

class PostUnknown extends Component
{
  render ()
  {
    return(
		<Container fluid>
			<h3>Unknown Post</h3>
			<pre>
				JSON.stringify(this.props.postData)
			</pre>
		</Container>
    );
  }
}

export default PostUnknown;
