# Generated from src/PythonSubset.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonSubsetParser import PythonSubsetParser
else:
    from PythonSubsetParser import PythonSubsetParser

# This class defines a complete generic visitor for a parse tree produced by PythonSubsetParser.

class PythonSubsetVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonSubsetParser#program.
    def visitProgram(self, ctx:PythonSubsetParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#functionDef.
    def visitFunctionDef(self, ctx:PythonSubsetParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#parameterList.
    def visitParameterList(self, ctx:PythonSubsetParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#statement.
    def visitStatement(self, ctx:PythonSubsetParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#assignmentStmt.
    def visitAssignmentStmt(self, ctx:PythonSubsetParser.AssignmentStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#printStmt.
    def visitPrintStmt(self, ctx:PythonSubsetParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#ifStmt.
    def visitIfStmt(self, ctx:PythonSubsetParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#whileStmt.
    def visitWhileStmt(self, ctx:PythonSubsetParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#returnStmt.
    def visitReturnStmt(self, ctx:PythonSubsetParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#block.
    def visitBlock(self, ctx:PythonSubsetParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:PythonSubsetParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#StringLiteral.
    def visitStringLiteral(self, ctx:PythonSubsetParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#Number.
    def visitNumber(self, ctx:PythonSubsetParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#MulDiv.
    def visitMulDiv(self, ctx:PythonSubsetParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#AddSub.
    def visitAddSub(self, ctx:PythonSubsetParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#Parens.
    def visitParens(self, ctx:PythonSubsetParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#Relational.
    def visitRelational(self, ctx:PythonSubsetParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#Id.
    def visitId(self, ctx:PythonSubsetParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#expressionList.
    def visitExpressionList(self, ctx:PythonSubsetParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSubsetParser#functionCall.
    def visitFunctionCall(self, ctx:PythonSubsetParser.FunctionCallContext):
        return self.visitChildren(ctx)



del PythonSubsetParser