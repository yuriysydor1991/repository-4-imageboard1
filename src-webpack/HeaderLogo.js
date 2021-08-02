import React, { Component} from "react";
import Navbar from "react-bootstrap/Navbar";

class HeaderLogo extends Component
{
  render ()
  {
    return(
		<Navbar.Brand href="/">
			<img
			alt="My Image Board logo"
			src="/assets/img/Picture_icon_BLACK.svg"
			width="30"
			height="30"
			className="d-inline-block align-top bg-white"
			/>{' '}
				My Image Board
		</Navbar.Brand>
    );
  }
}

export default HeaderLogo;
