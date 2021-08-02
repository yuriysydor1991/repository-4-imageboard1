import * as React from "react";
import { List, Datagrid, TextField, ReferenceField } from 'react-admin';

class CommentsList extends React.Component
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
					<ReferenceField source="post" reference="posts">
						<TextField source="title" />
					</ReferenceField>
					<TextField source="comment" />
					<TextField source="date" />
					<TextField source="updated" />
				</Datagrid>
			</List>
		);
	}
}

export default CommentsList