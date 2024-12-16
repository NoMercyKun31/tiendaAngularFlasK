-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-12-2024 a las 16:34:04
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda_angular_python_lunargames`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito`
--

CREATE TABLE `carrito` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  `id_videojuego` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fecha_agregado` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito`
--

INSERT INTO `carrito` (`id`, `id_usuario`, `id_videojuego`, `cantidad`, `fecha_agregado`) VALUES
(40, 1, 17, 1, '2024-12-13 15:31:21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_pedido`
--

CREATE TABLE `detalles_pedido` (
  `id` int(11) NOT NULL,
  `id_pedido` int(11) NOT NULL,
  `id_videojuego` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `direccion` text NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `numero_tarjeta` varchar(16) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `estado` varchar(20) DEFAULT 'pendiente',
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `ip_address` varchar(45) DEFAULT NULL COMMENT 'IPv4 or IPv6 address',
  `user_agent` varchar(255) DEFAULT NULL COMMENT 'Browser User-Agent string'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `videojuegos_retro`
--

CREATE TABLE `videojuegos_retro` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `estado` enum('En Oferta','Destacado','Nuevo Lanzamiento') NOT NULL,
  `compania` varchar(255) NOT NULL,
  `anio_lanzamiento` int(11) NOT NULL,
  `categoria` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `videojuegos_retro`
--

INSERT INTO `videojuegos_retro` (`id`, `titulo`, `precio`, `estado`, `compania`, `anio_lanzamiento`, `categoria`) VALUES
(1, 'Super Mario Bros.', 19.99, 'En Oferta', 'Nintendo', 1985, 'Plataformas'),
(2, 'Sonic the Hedgehog', 15.49, 'En Oferta', 'Sega', 1991, 'Plataformas'),
(3, 'The Legend of Zelda', 29.99, 'En Oferta', 'Nintendo', 1986, 'Aventura'),
(4, 'Pac-Man', 9.99, 'En Oferta', 'Namco', 1980, 'Arcade'),
(5, 'Street Fighter II', 24.99, 'En Oferta', 'Capcom', 1991, 'Lucha'),
(6, 'Donkey Kong', 14.99, 'En Oferta', 'Nintendo', 1981, 'Arcade'),
(7, 'Chrono Trigger', 39.99, 'Destacado', 'Square', 1995, 'RPG'),
(8, 'Final Fantasy VII', 44.99, 'Destacado', 'Square Enix', 1997, 'RPG'),
(9, 'Metal Gear Solid', 34.99, 'Destacado', 'Konami', 1998, 'Acción/Aventura'),
(10, 'Mega Man X', 29.99, 'Destacado', 'Capcom', 1993, 'Plataformas/Acción'),
(11, 'Castlevania: Symphony of the Night', 49.99, 'Destacado', 'Konami', 1997, 'Aventura/Plataformas'),
(12, 'Contra', 19.99, 'Destacado', 'Konami', 1987, 'Acción'),
(13, 'Shovel Knight', 34.99, 'Nuevo Lanzamiento', 'Yacht Club Games', 2014, 'Plataformas'),
(14, 'Cuphead', 39.99, 'Nuevo Lanzamiento', 'Studio MDHR', 2017, 'Acción/Plataformas'),
(15, 'Streets of Rage 4', 29.99, 'Nuevo Lanzamiento', 'Dotemu', 2020, 'Beat \'em up'),
(16, 'Celeste', 19.99, 'Nuevo Lanzamiento', 'Maddy Makes Games', 2018, 'Plataformas'),
(17, 'Hollow Knight', 24.99, 'Nuevo Lanzamiento', 'Team Cherry', 2017, 'Metroidvania'),
(18, 'Axiom Verge', 29.99, 'Nuevo Lanzamiento', 'Thomas Happ Games', 2015, 'Metroidvania'),
(22, 'Super Mario Bros 2 ', 21.95, 'Destacado', 'Nintendo', 1988, 'Plataformas');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_videojuego` (`id_videojuego`);

--
-- Indices de la tabla `detalles_pedido`
--
ALTER TABLE `detalles_pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_pedido` (`id_pedido`),
  ADD KEY `id_videojuego` (`id_videojuego`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `videojuegos_retro`
--
ALTER TABLE `videojuegos_retro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carrito`
--
ALTER TABLE `carrito`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `detalles_pedido`
--
ALTER TABLE `detalles_pedido`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `videojuegos_retro`
--
ALTER TABLE `videojuegos_retro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carrito`
--
ALTER TABLE `carrito`
  ADD CONSTRAINT `carrito_ibfk_1` FOREIGN KEY (`id_videojuego`) REFERENCES `videojuegos_retro` (`id`);

--
-- Filtros para la tabla `detalles_pedido`
--
ALTER TABLE `detalles_pedido`
  ADD CONSTRAINT `detalles_pedido_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `detalles_pedido_ibfk_2` FOREIGN KEY (`id_videojuego`) REFERENCES `videojuegos_retro` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
