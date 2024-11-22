INSERT_CIRCUIT = ("INSERT INTO Circuit"
                  "(circuit_id, name, country)"
                  "VALUES (%s, %s, %s)")

INSERT_CONSTRUCTOR = ("INSERT INTO Constructor"
                      "(constructor_id, name, country, date_of_first_debut, total_championships, total_race_entries, total_race_wins, total_points)"
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

INSERT_DRIVER = ("INSERT INTO Driver "
                 "(driver_id, name, dob, dod, gender, country_of_birth, "
                 "total_championships, total_race_entries, total_race_wins, total_points) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

INSERT_DRIVER_ENTRY = ("INSERT INTO DriverEntry"
                       "(driverEntry_id, driver_id, constructor_id, season_id, start_date, end_date, driver_role)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")

INSERT_GRAND_PRIX = ("INSERT INTO GrandPrix"
                     "(grandprix_id, circuit_id, season_id, qual_id, race_id, name, qualifying_format)"
                     "VALUES (%s, %s, %s, %s, %s, %s, %s)")

INSERT_MAIN_RACE = ("INSERT INTO MainRace"
                    "(race_id, grandprix_id, date)"
                    "VALUES (%s, %s, %s)")

INSERT_PIT_STOP = ("INSERT INTO PitStop"
                   "(pitstop_id, race_id, driver_id, lap_number, time_in_pit)"
                   "VALUES (%s, %s, %s, %s, %s)")

INSERT_QUALIFICATION_RACE = ("INSERT INTO QualificationRace"
                             "(qual_id, grandprix_id, date)"
                             "VALUES (%s, %s, %s)")

INSERT_QUALIFYING_RESULT = ("INSERT INTO QualifyingResult"
                            "(qualresult_id, driver_id, qual_id, best_time, gap, position)"
                            "VALUES (%s, %s, %s, %s, %s, %s)")

INSERT_RACE_RESULT = ("INSERT INTO RaceResult"
                      "(raceresult_id, race_id, driver_id, constructor_id, position, points_gain_loss, total_pit_stops)"
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)")

INSERT_SEASON = ("INSERT INTO Season"
                 "(season_id, driver_winner, constructor_winner)"
                 "VALUES (%s, %s, %s)")
