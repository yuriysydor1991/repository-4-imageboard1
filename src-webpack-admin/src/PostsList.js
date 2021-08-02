import * as React from "react";
import { List, Datagrid, TextField, ReferenceField } from 'react-admin';

class PostsList extends React.Component
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
					<ReferenceField source="user" reference="users">
						<TextField source="nickname" />
					</ReferenceField>
					<TextField source="type" />
					<TextField source="title" />
					<TextField source="url" />
					<TextField source="img" />
					<TextField source="meta_keywords" />
					<TextField source="meta_description" />
					<TextField source="views" />
					<TextField source="date" />
					<TextField source="updated" />
				</Datagrid>
			</List>
		);
	}
}

export default PostsList