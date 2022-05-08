-- Setup the user table

DROP TABLE user;

CREATE TABLE user (
        id INTEGER NOT NULL, 
        username VARCHAR, 
        email VARCHAR, 
        hashed_password VARCHAR, 
        is_active BOOLEAN, 
        PRIMARY KEY (id)
);

CREATE INDEX ix_user_id ON user (id);
CREATE UNIQUE INDEX ix_user_username ON user (username);
CREATE UNIQUE INDEX ix_user_email ON user (email);

-- Now add some data

INSERT INTO user
(
  id,
  username,
  email,
  hashed_password,
  is_active
)
VALUES
( 1, 'bilbo',     'bilbo.baggins@hobiton.net', 'some hash', 1),
( 2, 'frodo',     'frodo.baggins@hobiton.net', 'some hash', 1),
( 3, 'merry',     'meriadoc.brandybuck@hobiton.net', 'some hash', 1),
( 4, 'pippin',    'peregrin.took@hobiton.net', 'some hash', 1),
( 5, 'sam',       'samwise.gamgee@hobiton.net', 'some hash', 1),
( 6, 'gandalf',   'gandalf.the.grey@underwood.net', 'some hash', 1),
( 7, 'gollum',    'gollum@mordor.net', 'some hash', 1),
( 8, 'sauruman',  'saurum@the-tower.net', 'some hash', 1),
( 9, 'aragorn',   'aragorn@the-inn.net', 'some hash', 1),
(10, 'faramir',   'faramir@gondor.net', 'some hash', 1),
(11, 'boromir',   'boromir@gondor.net', 'some hash', 1),
(12, 'arwen',     'arwen.evenstar@rivendel.net', 'some hash', 1),
(13, 'birgil',    'birgil@minas-tirith.net', 'some hash', 1),
(14, 'denethor',  'denethor@moria.net', 'some hash', 1),
(15, 'elrond',    'elrond@rivendel.net', 'some hash', 1),
(16, 'gimli',     'gimli@moria.net', 'some hash', 1),
(17, 'legolas',   'legolas@rivendel.net', 'some hash', 1),
(18, 'galadriel', 'galadriel@lothlorien.net', 'some hash', 1),
(19, 'celeborn',  'celeborn@lothlorien.net', 'some hash', 1),
(20, 'radagast',  'radagast@fangorn.net', 'some hash', 1),
(21, 'sauron',    'sauron@mordor.net', 'some hash', 1),
(22, 'cirion',    'steward.of.gondor@gondor.net', 'some hash', 1),
(23, 'théoden',   'king.of.rohan@rohan.net', 'some hash', 1);
