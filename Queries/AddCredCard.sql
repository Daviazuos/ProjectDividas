INSERT INTO "Cards" ("cardname",
                      "duedate",
                      "closure",
                      "cardstatus")
VALUES(%s, %s, %s, %s) RETURNING cardid