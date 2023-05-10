
//use teste


// Create a new collection teacher.
db.createCollection('user', {
    validator:{
        $jsonSchema:{
            bsonType: 'object',
            required: ['username', 'password', 'email', 'is_customer', 'languages'],
            properties:{
                username: {
                    bsonType: 'string'
                },
                password: {
                    bsonType: 'string'
                },
                email: {
                    bsonType: 'string'
                },
                first_name: {
                    bsonType: 'string'
                },
                last_name: {
                    bsonType: 'string'
                },
                phone: {
                    bsonType: 'string'
                },
                address: {
                    bsonType: 'object',
                    properties: {
                        street: {
                            bsonType: 'string'
                        },
                        number: {
                            bsonType: 'int'
                        },
                        city: {
                            bsonType: 'string'
                        },
                        state: {
                            bsonType: 'string'
                        },
                        country: {
                            bsonType: 'string'
                        },
                        zip: {
                            bsonType: 'string'
                        }
                    }

                },
                languages: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'string'
                    }  
                },
                is_customer: {
                    bsonType: 'bool'
                },
                teachers: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'objectId'
                    }
                },
                notes: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'objectId'
                    }
                },
                students: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'objectId'
                    }
                }
            }
        
        }
    }   
});


// Create a new collection student.
db.createCollection('student', {
    validator:{
        $jsonSchema:{
            bsonType: 'object',
            required: ['username', 'password', 'email'],
            properties:{
                username: {
                    bsonType: 'string'
                },
                password: {
                    bsonType: 'string'
                },
                email: {
                    bsonType: 'string'
                },
                phone: {
                    bsonType: 'string'
                },
                teachers: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'objectId'
                    }
                },
                notes: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'objectId'
                    }
                },
                address: {
                    bsonType: 'object',
                    properties: {
                        street: {
                            bsonType: 'string'
                        },
                        number: {
                            bsonType: 'int'
                        },
                        city: {
                            bsonType: 'string'
                        },
                        state: {
                            bsonType: 'string'
                        },
                        country: {
                            bsonType: 'string'
                        },
                        zip: {
                            bsonType: 'string'
                        }
                    }

                }
            }
        }
        
        }
    }
);


// Create a new collection note.
db.createCollection('note', {
    validator:{
        $jsonSchema:{
            bsonType: 'object',
            required: ['date'],
            properties:{
                date: {
                    bsonType: 'date'
                },
                themes: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'string'
                    }
                },
                new_words: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'objectId'
                    }
                },
                pronunciation: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'object'
                    }
                },
                rocked_when_i_say: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'string'
                    }
                },
                review: {
                    bsonType: 'array',
                    items: {
                        bsonType: 'string'
                    }
                }
            }
        }
    }
});


// Create a new collection new_word_cards.
db.createCollection('cards', {
    validator:{
        $jsonSchema:{
            bsonType: 'object',
            required: ['in_portuguese', 'in_english', 'rating'],
            properties:{
                in_portuguese: {
                    bsonType: 'string'
                },
                in_english: {
                    bsonType: 'string'
                },
                rating: {
                    bsonType: 'int'
                }
            }
        }
    }
});
