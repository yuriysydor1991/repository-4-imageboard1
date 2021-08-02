import React, { Component} from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import HeaderMenu from "./HeaderMenu.js";
import HeaderLogin from "./HeaderLogin.js";

class Header extends Component
{
  render ()
  {
    return(
		<Container fluid>
			<HeaderMenu></HeaderMenu>
		</Container>
    );
  }
}

export default Header;
