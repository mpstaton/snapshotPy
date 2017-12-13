
from models.variableDocumentation import VariableDocumentation

newVarDoc = VariableDocumentation(handle='test', inputVariations=['inputvar1', 'inputvar2'])

newVarDoc.addToDB()
