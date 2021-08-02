import React, { Component} from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav"
import HeaderLogo from "./HeaderLogo.js";
import Container from "react-bootstrap/Container";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHome } from '@fortawesome/free-solid-svg-icons'
import { faSignInAlt } from '@fortawesome/free-solid-svg-icons'

class HeaderMenu extends Component
{
  render ()
  {
    return(
		<Navbar bg="dark" variant="dark">
			<Container>
				<Navbar.Toggle aria-controls="basic-navbar-nav" />
				<Navbar.Collapse id="basic-navbar-nav">
				  <Nav className="me-auto">
					<Nav.Link href="/">
						<FontAwesomeIcon icon={faHome} />
						{' '} Home
					</Nav.Link>
					<Nav.Link href="/login">
						<FontAwesomeIcon icon={faSignInAlt} />
						{' '} Login
					</Nav.Link>
				  </Nav>
				</Navbar.Collapse>
				<HeaderLogo></HeaderLogo>
			</Container>
		</Navbar>
    );
  }
}

export default HeaderMenu;
