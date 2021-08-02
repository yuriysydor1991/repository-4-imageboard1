import React, { Component} from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Header from "./Header.js";
import Footer from "./Footer.js";
import LoginForm from "./LoginForm.js";
import ServerResponse from "./ServerResponse.js";
import "./css/AppLogin.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

class AppLogin extends Component
{
  constructor(props)
  {
	  super(props);
	  
	  this.state = {
		  user: null
	  };
  }
  
  render ()
  {	
    return (
      <Container >
        <Header />
		<LoginForm user={this.state.user} />
		<Footer />
      </Container>
    ) ;
  }
  
  componentDidMount () 
  {
    fetch("/rest/v1/general/signin_content")
      .then(res => res.json())
      .then(
        (result) => {
		  console.log("Fetched server result:");
		  console.log(result);
		  
		  let checker = new ServerResponse();
		  
		  if (checker.check(result))
		  {
			  this.setState({
				user: result.content.user
			  });
		  }
		  else
			  console.log ('Unrecognized server response! ', result);
        },
        // Примітка: важливо обробляти помилки саме тут,
        // а не в блоці catch (), щоб не перехоплювати
        // виключення з помилок в самих компонентах.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }
}

export default AppLogin;
