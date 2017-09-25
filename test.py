class Bus {
	property middlewares = []

	function run(Command) {
		for(middleares as middleware) {
			new middlware(Command);
		}
	}
}

class Middleware1 {
	function constructor(Command) {
		var x ;
	}
}

class Bus {
	property middlewares = []

	function run(Command) {
		for(middleares as middleware) {
			middlware.excute(Command);
		}
	}
}

class Middleware1 {
	property x;
	function constructor(xxxx) {

	}

	function execute(Command) {
		if (Command != xxx) {
			return;
		}

		this.x.bar(command)
	}
}


class CommandA {
	property type = 'vdo';
	property cmd = '/abc';

	function checkCmd(cmd) {
		.....
	}
}

class CommandA {
	property type = 'vdo';
	property cmd = '';


}


dependency injection

