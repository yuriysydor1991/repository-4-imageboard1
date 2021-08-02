import * as React from "react";
import { Admin, Resource } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
import UsersList from './UsersList.js';
import PostsList from './PostsList.js';
import CommentsList from './CommentsList.js';
import UserCreate from './UserCreate.js';
import PostCreate from './PostCreate.js';
import UserIcon from '@material-ui/icons/Group';

class App extends React.Component
{
	constructor (props)
	{
		super(props)
		
		let myU = jsonServerProvider('http://192.168.88.246:6543/rest/v1-react-admin')
		let test = jsonServerProvider('https://jsonplaceholder.typicode.com')
		
		this.state = {
			usersDataProvider: myU,
		}
	}
	
	render () {
		return (
			<Admin dataProvider={this.state.usersDataProvider}>
				<Resource name="users" list={UsersList} create={UserCreate} />
				<Resource name="posts" list={PostsList} create={PostCreate}/>
				<Resource name="comments" list={CommentsList} />
			</Admin>
		);
	}
}

export default App;
