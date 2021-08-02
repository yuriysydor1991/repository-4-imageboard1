class ServerResponse
{
	check (jsonResponse)
	{
		console.log ("Checking response: ", jsonResponse);
		
		if (   !jsonResponse.hasOwnProperty('status')
			|| !jsonResponse.hasOwnProperty('app')
			|| !jsonResponse.hasOwnProperty('version')
			|| jsonResponse.app != 'MyImageBoard'
			|| jsonResponse.version !== '1'
		)
		{ return false; }
		
		return true;
	}
}

export default ServerResponse;