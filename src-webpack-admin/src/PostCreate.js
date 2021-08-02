import * as React from "react";
import { 
		TextInput, ReferenceInput, SelectInput,
		ReferenceField, Create, SimpleForm,
		ImageInput, ImageField
	} from 'react-admin';

class PostCreate extends React.Component
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
					<TextInput source="title" fullWidth={true} />
					<TextInput source="meta_keywords" fullWidth={true} />
					<TextInput source="meta_description" fullWidth={true} />
					<ReferenceInput source="user" reference="users">
						<SelectInput optionText="email" />
					</ReferenceInput>
					<SelectInput source="type" choices={[
						{ id: 'image-regular', name: 'Image Regular' },
					]} />
					<TextInput source="url" />
					<ImageInput source="img" label="Related pictures" accept="image/*">
						<ImageField source="src" title="title" />
					</ImageInput>
				</SimpleForm>
			</Create>
		);
	}
}

export default PostCreate;

/*
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
user INT DEFAULT NULL,
type VARCHAR(128) DEFAULT 'image-regular',
title VARCHAR(128) DEFAULT NULL,
url VARCHAR(128) DEFAULT NULL,
img VARCHAR(1024) DEFAULT NULL,
meta_keywords VARCHAR(1024) DEFAULT NULL,
meta_description VARCHAR(1024) DEFAULT NULL,
views INT DEFAULT 0,
date TIMESTAMP DEFAULT current_timestamp(),
updated TIMESTAMP DEFAULT current_timestamp() ON UPDATE current_timestamp(),
*/