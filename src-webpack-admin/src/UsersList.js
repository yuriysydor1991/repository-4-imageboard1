import * as React from "react";
import { List, Datagrid, TextField, EmailField, EditButton } from 'react-admin';

class UsersList extends React.Component
{
	constructor(props)
	{
		super(props);
	}
	
	render ()
	{
		return  (
			<List {...this.props}>
				<Datagrid rowClick="edit">
					<TextField source="id" />
					<TextField source="nickname" />
					<TextField source="password" />
					<EmailField source="email" />
					<TextField source="logo" />
					<TextField source="website" />
					<TextField source="date" />
					<TextField source="updated" />
					<EditButton />
				</Datagrid>
			</List>
		);
	}
}

export default UsersList