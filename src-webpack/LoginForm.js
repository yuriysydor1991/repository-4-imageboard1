import React, { Component} from "react";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Alert from "react-bootstrap/Alert";
import "./css/LoginForm.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee } from '@fortawesome/free-solid-svg-icons'

class LoginForm extends Component
{
  constructor (props)
  {
	super(props)

	this.state = {
	  nick: '',
	  pass: ''
	}

	this.nickChange = this.nickChange.bind(this);
	this.passChange = this.passChange.bind(this);
	this.sign_in_action = this.sign_in_action.bind(this);
  }
  
  render ()
  {
	if (this.props.user)
		return (
			<Container fluid >
				<div className="LoginForm bg-dark border border-dark rounded">
					<Alert variant="dark">
						<Alert.Heading>
							<FontAwesomeIcon icon={faCoffee} />
							Hey, nice to see you
						</Alert.Heading>
						<p>
							You are logged in as {this.props.user.nickname}
							({this.props.user.email})
						</p>
					</Alert>
				</div>
			</Container>
	);
	
    return(
		<Container fluid >
			
				<Form className="LoginForm bg-dark border border-dark rounded"
					  onSubmit={this.sign_in_action}
				>
				
				  <Form.Group className="mb-3" controlId="formBasicEmail">
					<Form.Label className="text-white">Login</Form.Label>
					<Form.Control 	as="input" type="text"
									placeholder="Enter your login" 
									onChange={this.nickChange}
									value={this.state.nick}
					/>
				  </Form.Group>

				  <Form.Group className="mb-3" controlId="formBasicPassword">
					<Form.Label className="text-white">Password</Form.Label>
					<Form.Control 	type="password" 
									placeholder="Enter your password" 
									onChange={this.passChange}
									value={this.state.pass}
					/>
				  </Form.Group>
				  
				  <Button variant="primary" type="submit btn-block" size="lg">
					Login
				  </Button>
				  
				</Form>
		</Container>
    );
  }
  
  nickChange()
  {
	  this.setState({nick: event.target.value});
  }
  
  passChange()
  {
	  this.setState({pass: event.target.value});
  }
  
  sign_in_action(e)
  {
	  e.preventDefault();
	  
	  location.href= "/signin?login=" + encodeURIComponent(this.state.nick)
					 + '&password=' + encodeURIComponent(this.state.pass)
  }
}

export default LoginForm;