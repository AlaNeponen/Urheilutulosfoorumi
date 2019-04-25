As a/an | I want to | so that | required query
--- | --- | --- | ---
user | add my favourite team's results | i can talk about them with other fans | INSERT INTO Match (winner, opponent, date_when, score, event, account_id) VALUES (... , current_user.id);
user | register an account | people can recognize my comments from my username | INSERT INTO account (date_created, date_modified, username, password, role) VALUES (... , 'PLEB');
user | edit or delete my account | I can have control over my account | *many queries, ex.* SELECT * FROM Comment WHERE account_id = current_user.id); & DELETE FROM Comment WHERE (id = comment_id);  *where comment_id is gotten from a list of comments, created using the previous query*. 
admin | remove/edit false results | the site won't have falsified information | REMOVE FROM Comment WHERE (matchid = id_of_the_match_in_question); & REMOVE FROM Match WHERE (id = id_of_the_match_in_question);
admin | remove offensive comments | the discussion will remain civilized | REMOVE FROM Comment WHERE (id = id_of_the_comment_in_question); 
