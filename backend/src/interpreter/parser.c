#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "lexer.h"
#include "parser.h"

void lexer_next_token(TOKEN_NODE **token_node, TOKEN **token) {
    *token = &(*token_node)->currentToken;
    *token_node = (*token_node)->nextToken;
}

bool expected_token_type(TOKEN_TYPE actualType, TOKEN_TYPE expectedType) {
    if (actualType != expectedType) {
        fprintf(stderr, "Error: Expected %d, got %d\n", expectedType, actualType);
        fprintf(stderr, "Error: Expected %d, got %d\n", expectedType, actualType);
        return false;
    }
    return true;
}

AST* parse(TOKEN_NODE *token_node) {

    AST *ast = malloc(sizeof(AST));
    TOKEN *token = NULL;

    // lexer_next_token(&token_node, &token);
    // if (!expected_token_type(token->type, WHERE)) {
    //     return NULL;
    // }
    // WHERE_IDENTIFIER where_identifier;
    // where_identifier.where_condition_token = token;

    // WHERE_IDENTIFIER_NODE *where_identifier_node = malloc(sizeof(WHERE_IDENTIFIER_NODE));
    // where_identifier_node->where_identifier = where_identifier;
    // where_identifier_node->next_where_identifier = NULL;
    
    // ast->where_identifier_list = where_identifier_node;


    CHART_IDENTIFIER_NODE chart_identifier_node;

    lexer_next_token(&token_node, &token);
    if (!expected_token_type(token->type, CHART)) {
        return NULL;
    }

    lexer_next_token(&token_node, &token);
    if (!expected_token_type(token->type, CHARTED_TOKEN_TYPE)) {
        return NULL;
    }
    chart_identifier_node.charted_token = token;


    lexer_next_token(&token_node, &token);
    if (!expected_token_type(token->type, IN)) {
        return NULL;
    }


    lexer_next_token(&token_node, &token);
    if (!expected_token_type(token->type, CHART_TYPE)) {
        return NULL;
    }
    chart_identifier_node.chart_type_token = token;

    lexer_next_token(&token_node, &token);
    if (!expected_token_type(token->type, FOR)) {
        return NULL;
    }

    lexer_next_token(&token_node, &token);
    if (expected_token_type(token->type, AGGREGATE)) {
        chart_identifier_node.x_axis_aggregate_token = token;
        lexer_next_token(&token_node, &token);
    } else {
        chart_identifier_node.x_axis_aggregate_token = NULL;
    }

    if (!expected_token_type(token->type, AXIS_TOKEN_TYPE)) {
        return NULL;
    }
    chart_identifier_node.x_axis_token = token;

    lexer_next_token(&token_node, &token);
    if (!expected_token_type(token->type, VS)) {
        return NULL;
    }

    lexer_next_token(&token_node, &token);
    if (expected_token_type(token->type, AGGREGATE)) {
        chart_identifier_node.y_axis_aggregate_token = token;
        lexer_next_token(&token_node, &token);
    } else {
        chart_identifier_node.y_axis_aggregate_token = NULL;
    }

    if (!expected_token_type(token->type, AXIS_TOKEN_TYPE)) {
        return NULL;
    }
    chart_identifier_node.y_axis_token = token;
    ast->chart_identifier = chart_identifier_node;

    
    bool first_where = true;
    WHERE_IDENTIFIER_NODE *where_identifier_node;

    while (token_node != NULL) {

        WHERE_IDENTIFIER where_identifier;

        if (first_where) {
            lexer_next_token(&token_node, &token);
            if (!expected_token_type(token->type, WHERE)) {
                return NULL;
            }
        } else {
            lexer_next_token(&token_node, &token);
            if (!expected_token_type(token->type, AND)) {
                return NULL;
            }
        }

        lexer_next_token(&token_node, &token);
        if (!expected_token_type(token->type, AXIS_TOKEN_TYPE)) {
            return NULL;
        }
        where_identifier.where_field_token = token;

        lexer_next_token(&token_node, &token);
        if (!expected_token_type(token->type, EQUALS)) {
            return NULL;
        }

        lexer_next_token(&token_node, &token);
        if (!expected_token_type(token->type, WHERE_VALUE)) {
            return NULL;
        }

        where_identifier.where_condition_token = token;
        
        if (first_where) {
            where_identifier_node = malloc(sizeof(WHERE_IDENTIFIER_NODE));
            where_identifier_node->where_identifier = where_identifier;
            where_identifier_node->next_where_identifier = NULL;
            
            ast->where_identifier_list = where_identifier_node;

            first_where = false;
        } else {
            WHERE_IDENTIFIER_NODE *next_where_identifier_node = malloc(sizeof(WHERE_IDENTIFIER_NODE));
            next_where_identifier_node->where_identifier = where_identifier;
            next_where_identifier_node->next_where_identifier = NULL;

            where_identifier_node->next_where_identifier = next_where_identifier_node;
            where_identifier_node = next_where_identifier_node;
        }

    }
    
    return ast;
}

void print_ast(AST *ast) {
    printf("Token type in AST: %s\n", type_to_string(ast->chart_identifier.charted_token->type));
    printf("Token type in AST: %s\n", type_to_string(ast->chart_identifier.chart_type_token->type));
    printf("Token type in AST: %s\n", type_to_string(ast->chart_identifier.x_axis_token->type));
    printf("Token type in AST: %s\n", type_to_string(ast->chart_identifier.y_axis_token->type));
    
    WHERE_IDENTIFIER_NODE *temp_where_identifier_list = ast->where_identifier_list;
            
    while (temp_where_identifier_list != NULL) {
        printf("Token type in AST: %s, value:%s\n", type_to_string(temp_where_identifier_list->where_identifier.where_condition_token->type), temp_where_identifier_list->where_identifier.where_condition_token->content);
        temp_where_identifier_list = temp_where_identifier_list->next_where_identifier;
    }
    // printf("Token type in AST: %s, value:%s\n", type_to_string(ast->where_identifier_list->where_identifier.where_condition_token->type), ast->where_identifier_list->where_identifier.where_condition_token->content);

    printf("\n");
}

void free_ast(AST *ast) {

    CHART_IDENTIFIER_NODE chart_node = ast->chart_identifier;

    free(chart_node.charted_token);
    free(chart_node.chart_type_token);
    free(chart_node.x_axis_token);
    free(chart_node.y_axis_token);


    WHERE_IDENTIFIER_NODE *where_node_head = ast->where_identifier_list;
    WHERE_IDENTIFIER_NODE *tmp;

   while (where_node_head != NULL)
    {
       tmp = where_node_head;
       where_node_head = where_node_head->next_where_identifier;
       free(tmp->where_identifier.where_field_token);
       free(tmp->where_identifier.where_condition_token);
       free(tmp);
    }
    
    free(ast);
}