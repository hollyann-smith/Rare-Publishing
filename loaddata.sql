CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);


INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');



INSERT INTO `Users` VALUES (null, "John", "Doe", "jd45@gmail.com", "I am a tractor guy", "johndoe", "portaJohn", "https://randomuser.me/api/portraits/men/1.jpg", "2020-01-01", 1);
INSERT INTO `Users` VALUES (null, "Jane", "Doe", "jd44@gmail.com", "I am a tractor chick", "janedoe", "portaJane", "https://randomuser.me/api/portraits/women/1.jpg", "2020-01-01", 1);
INSERT INTO `Users` VALUES (null, "Jerry", "Doe", "jd43@gmail.com", "I am a tractor ccousin", "jerrydoo", "portaJerry", "https://randomuser.me/api/portraits/men/2.jpg", "2020-01-01", 1);
INSERT INTO `Users` VALUES (null, "Jessica", "Doe", "jd42@gmail.com", "I am a tractor grandma", "jessicadoe", "portaJessica", "https://randomuser.me/api/portraits/women/2.jpg", "2020-01-01", 1);
INSERT INTO `Users` VALUES (null, "Jack", "Doe", "jd41@gmail.com", "I am a tractor grandpa", "jackdoe", "portaJack", "https://randomuser.me/api/portraits/men/3.jpg", "2020-01-01", 1);
INSERT INTO `Users` VALUES (null, "Johnny", "Doe", "jd40@gmail.com", "I am a tractor grandson", "johnnydoo", "portaJohnny", "https://randomuser.me/api/portraits/men/4.jpg", "2020-01-01", 1);

INSERT INTO `Posts` VALUES (null, 1, 1, "Tractor News", "2020-01-01", "https://picsum.photos/200/300", "This is a tractor news", 1);
INSERT INTO `Posts` VALUES (null, 2, 1, "Tractor Blues", "2020-06-01", "https://picsum.photos/200/301", "This is a tractortastrophe", 1);
INSERT INTO `Posts` VALUES (null, 3, 1, "Tractor Facts", "2020-03-01", "https://picsum.photos/200/302", "This is a tractor fact", 1);
INSERT INTO `Posts` VALUES (null, 4, 1, "Tractor Facts", "2020-03-01", "https://picsum.photos/200/303", "This is a tractor fact", 1);
INSERT INTO `Posts` VALUES (null, 5, 1, "Tractor Facts", "2020-03-01", "https://picsum.photos/200/304", "This is a tractor fact", 1);
INSERT INTO `Posts` VALUES (null, 6, 1, "Tractor Facts", "2020-03-01", "https://picsum.photos/200/305", "This is a tractor fact", 1);

INSERT INTO `Comments` VALUES (null, 2, 1, "This is a comment");
INSERT INTO `Comments` VALUES (null, 4, 2, "This is a comment");
INSERT INTO `Comments` VALUES (null, 6, 3, "This is a comment");
INSERT INTO `Comments` VALUES (null, 3, 4, "This is a comment");
INSERT INTO `Comments` VALUES (null, 5, 5, "This is a comment");

INSERT INTO `Categories` VALUES (null, "News");
INSERT INTO `Categories` VALUES (null, "Facts");
INSERT INTO `Categories` VALUES (null, "Blues");
INSERT INTO `Categories` VALUES (null, "Tastrophe");
INSERT INTO `Categories` VALUES (null, "Fiction");
INSERT INTO `Categories` VALUES (null, "History");


SELECT
  c.id,
  c.label
FROM Categories c
WHERE c.id = 1

-- Select Category ID 1
SELECT
  c.id,
  c.label
FROM Categories c
WHERE c.id = 1
