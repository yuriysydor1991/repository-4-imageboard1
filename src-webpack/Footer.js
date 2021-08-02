import React, { Component} from "react";
import Container from "react-bootstrap/Container";
import "./css/Footer.css";

class Footer extends Component
{
  render ()
  {
    return(
		<Container fluid className="footerWrapper">
			<span className="text text-muted">
				Copyright &copy; Sydor Yuriy, 2021 (
				<a href="mailto:yurisydor1991@gmail.com"
				   className="text text-muted"
				>
					yurisydor1991@gmail.com
				</a>
				)
			</span>
		</Container>
    );
  }
}

export default Footer;
