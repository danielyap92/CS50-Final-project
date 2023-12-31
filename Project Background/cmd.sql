CREATE TABLE periodic_service(
    n INTEGER PRIMARY KEY NOT NULL,
    engine_oil INTEGER NOT NULL,
    engine_oil_filter INTEGER NOT NULL,
    drain_plug_gasket INTEGER NOT NULL,
    spark_plug INTEGER NOT NULL,
    air_filter INTEGER NOT NULL,
    radiator_coolant INTEGER NOT NULL,
    brake_fluid INTEGER NOT NULL,
    fuel_filter INTEGER NOT NULL,
    transmission_oil_cvt INTEGER NOT NULL,
    transmission_oil_filter INTEGER NOT NULL,
    gasket_oil_pan INTEGER NOT NULL,
    drain_plug INTEGER NOT NULL,
    timing_belt_kit INTEGER NOT NULL,
    fead_belt INTEGER NOT NULL,
    Timestamp DATETIME DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime'))
);

INSERT INTO periodic_service (
n,engine_oil,engine_oil_filter,drain_plug_gasket,spark_plug,air_filter,radiator_coolant,brake_fluid,fuel_filter,transmission_oil_cvt,transmission_oil_filter,gasket_oil_pan,drain_plug,timing_belt_kit,fead_belt)
VALUES
(1,1,1,1,0,0,0,0,0,0,0,0,0,0,0),
(2,1,1,1,0,0,0,0,0,0,0,0,0,0,0),
(3,1,1,1,0,1,0,0,0,0,0,0,0,0,0),
(4,1,1,1,1,0,0,0,1,0,0,0,0,0,0),
(5,1,1,1,0,1,0,1,0,0,0,0,0,0,0),
(6,1,1,1,0,0,0,0,0,0,0,0,0,0,0),
(7,1,1,1,1,1,0,0,1,1,1,0,1,0,0),
(8,1,1,1,0,0,0,0,0,0,0,0,0,0,0),
(9,1,1,1,0,1,0,1,0,0,0,0,0,0,0),
(10,1,1,1,1,0,1,0,1,0,0,0,0,0,0),
(11,1,1,1,0,1,0,0,0,0,0,0,0,0,1),
(12,1,1,1,0,0,0,0,0,0,0,0,0,1,0),
(13,1,1,1,1,1,0,1,1,1,1,1,1,0,0),
(14,1,1,1,0,0,0,0,0,0,0,0,0,0,0),
(15,1,1,1,0,1,0,0,0,0,0,0,0,0,0),
(16,1,1,1,1,0,0,0,1,0,0,0,0,0,0);
-- SELECT * FROM periodic_service ORDER BY n DESC LIMIT 1;
