CREATE TABLE `rodeos` (
  `id` int PRIMARY KEY,
  `nombre` varchar(255),
  `peso_min` decimal,
  `peso_max` decimal
);

CREATE TABLE `caravanas` (
  `caravana` varchar(255) PRIMARY KEY,
  `fecha_alta` date,
  `fecha_baja` date,
  `razon_baja` varchar(255),
  `activa` bool,
  `rodeo_id` int
);

CREATE TABLE `pesajes` (
  `id` int PRIMARY KEY,
  `caravana` varchar(255),
  `peso` decimal,
  `fecha` date
);

ALTER TABLE `caravanas` ADD FOREIGN KEY (`rodeo_id`) REFERENCES `rodeos` (`id`);

ALTER TABLE `pesajes` ADD FOREIGN KEY (`caravana`) REFERENCES `caravanas` (`caravana`);
