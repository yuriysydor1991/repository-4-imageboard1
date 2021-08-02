import * as React from "react";
import { 
		TextInput, ReferenceInput, SelectInput,
		ReferenceField, Create, SimpleForm,
		ImageInput, ImageField
	} from 'react-admin';

class CommentCreate extends React.Component
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
					<ReferenceInput source="user" reference="users">
						<SelectInput optionText="email" />
					</ReferenceInput>
					<TextInput source="password" />
					<TextInput source="email" />
					<TextInput source="website" />
				</SimpleForm>
			</Create>
		);
	}
}

export default CommentCreate;