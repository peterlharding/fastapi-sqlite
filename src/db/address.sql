-- Setup the address table

DROP TABLE address;

CREATE TABLE address (
        id INTEGER NOT NULL, 
        address VARCHAR, 
        city VARCHAR, 
        state VARCHAR, 
        postcode VARCHAR, 
        coordinates VARCHAR, 
        owner_id INTEGER, 
        when_created DATETIME, 
        when_updated DATETIME, 
        PRIMARY KEY (id), 
        FOREIGN KEY(owner_id) REFERENCES user (id)
);

CREATE INDEX ix_address_id ON address (id);
CREATE INDEX ix_address_coordinates ON address (coordinates);
CREATE INDEX ix_address_address ON address (address);


