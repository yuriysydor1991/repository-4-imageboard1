import * as React from "react";
import { 
		TextInput, ReferenceInput,
		ReferenceField, Create, SimpleForm 
	} from 'react-admin';

class UserCreate extends React.Component
{
	constructor(props)
	{
		super(props)
	}
	
	render ()
	{
		return (
			<Create {...this.props}>
				<SimpleForm>
					<TextInput source="nickname" />
					<TextInput source="password" />
					<TextInput source="email" />
					<TextInput source="website" />
				</SimpleForm>
			</Create>
		);
	}
}

export default UserCreate;