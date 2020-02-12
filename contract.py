
contractABI= [
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_rounds",
				"type": "uint256"
			}
		],
		"name": "createTask",
		"outputs": [],
		"payable": True,
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "_user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "_fileHash",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			}
		],
		"name": "fileAdded",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "taskID",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			}
		],
		"name": "modelUpdated",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "taskID",
				"type": "uint256"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "_user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_amt",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "_time",
				"type": "uint256"
			}
		],
		"name": "newTaskCreated",
		"type": "event"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "string",
				"name": "_fileHash",
				"type": "string"
			}
		],
		"name": "storeFile",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_taskID",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_modelHash",
				"type": "string"
			},
			{
				"internalType": "address payable",
				"name": "computer",
				"type": "address"
			}
		],
		"name": "updateModelForTask",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getFiles",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getTaskCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_taskID",
				"type": "uint256"
			}
		],
		"name": "getTaskHashes",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getTasksOfUser",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "SentinelTasks",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "taskID",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "currentRound",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "totalRounds",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "cost",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "UserFiles",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "UserTaskIDs",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
];
contractAddress = "0x2317d8504FdC96De4Ee82DfEd023B54cBBed1AE3";
