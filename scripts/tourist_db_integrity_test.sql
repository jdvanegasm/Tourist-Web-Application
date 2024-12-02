insert into users (name, email, hashed_password) 
values 
('Juan Pérez', 'juan@example.com', '$2b$12$eImiTXuWVxfM37uY4JANjQpC.Ww9/Xzjph1cRloAeW2rUShJ0P0i'), -- password123
('Ana Gómez', 'ana@example.com', '$2b$12$5TpvX3HVxFejfFOphuX2U.f9tiUoFngCeh2ASiC4RyMi54gyRJDxu'), -- securePass1
('Carlos Rivera', 'carlos@example.com', '$2b$12$wJfYZ5JxO9OGKfJ6Ek/ae.X2DJOS3JbMInX9V9b0L9K92m4rv6/ry'), -- anotherPass
('Laura Torres', 'laura@example.com', '$2b$12$FZpynpAb0A8eUNpZXuH50O11d7AqWeA7jUJScOHoIRaRfiJ6gFQ2C'), -- 123secure
('Sofía Mendoza', 'sofia@example.com', '$2b$12$/uHQc5jJrEQ1h9MvDShPyuovPd/EM3Dl.K5EfoZXOFNuvPcG9mS/G'); -- myPassword

insert into countries (name) 
values 
('Colombia'), 
('Perú'), 
('México'), 
('Argentina'), 
('Chile');

insert into cities (name, country_id) 
values 
('Bogotá', 1), 
('Medellín', 1), 
('Lima', 2), 
('Cusco', 2), 
('Ciudad de México', 3);

insert into posts (title, description, city_id, user_id) 
values 
('Monserrate', 'Un mirador en Bogotá con vistas impresionantes.', 1, (select user_id from users where name = 'Juan Pérez')),
('Parque Explora', 'Un museo interactivo en Medellín.', 2, (select user_id from users where name = 'Carlos Rivera')),
('Machu Picchu', 'Una ciudadela inca en Perú.', 3, (select user_id from users where name = 'Ana Gómez')),
('Lago Humantay', 'Una laguna turquesa en Cusco.', 4, (select user_id from users where name = 'Sofía Mendoza')),
('Chichén Itzá', 'Un sitio arqueológico maya en México.', 5, (select user_id from users where name = 'Laura Torres'));

insert into tags (name) 
values 
('Aventura'), 
('Cultura'), 
('Naturaleza'), 
('Historia'), 
('Familia');

insert into post_tags (post_id, tag_id) 
values 
(1, 1), -- Monserrate con etiqueta "Aventura"
(2, 5), -- Parque Explora con etiqueta "Familia"
(3, 2), -- Machu Picchu con etiqueta "Cultura"
(4, 3), -- Lago Humantay con etiqueta "Naturaleza"
(5, 4); -- Chichén Itzá con etiqueta "Historia"

insert into images (url, post_id) 
values 
('https://monserrate.co/uploads/site/home/night-view-2x.jpg', 1), 
('https://www.parqueexplora.org/_next/image?url=https%3A%2F%2Fcdn.cosmicjs.com%2F1181a7f0-b1cb-11ec-97bc-19d12908cbbe-sobrelacorporacion.jpeg%3Ffit%3Dcrop%26w%3D1542%26h%3D700&w=3840&q=75', 2), 
('https://viajes.nationalgeographic.com.es/medio/2018/03/01/machu-picchu_5ff969ae_1280x720.jpg', 3), 
('https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/0d/16/0c/peruvian-andes-are-perfect.jpg?w=1200&h=-1&s=1', 4), 
('https://upload.wikimedia.org/wikipedia/commons/a/aa/Kukulk%C3%A1n_rodeada_de_azul..JPG', 5);