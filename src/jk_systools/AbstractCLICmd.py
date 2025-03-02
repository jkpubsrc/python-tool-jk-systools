

import os
import typing

import jk_typing
import jk_utils
import jk_logging
import jk_json
import jk_prettyprintobj
import jk_argparsing



class AbstractCLICmd(object):

	################################################################################################################################
	## Constants
	################################################################################################################################

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self,
		):
		
		pass
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def cliCmdName(self) -> str:
		raise NotImplementedError()
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def registerCLICommand(self, argsParser:jk_argparsing.ArgsParser) -> None:
		raise NotImplementedError()
	#

	def execute(self, appRuntime, *cmdArgs, log:jk_logging.AbstractLogger) -> int:
		raise NotImplementedError()
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	################################################################################################################################
	## Public Static Methods
	################################################################################################################################

#






