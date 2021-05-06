<b>Зачем это нужно?</b>
<br>
        Если вы хотите разработать приложение, в котором пользователь должен подтвердить емеил, а также реализовать базовые функции кабинета пользователя, такие как регистрация/активация аккаунта/сброс пароля и подобные, Вам незачем каждый раз писать один и тот же код, 
который реализует эти функции. Просто скопируйте этот репозиторий и Вы получите приложение с необходимым БАЗОВЫМ функционалом.
Также в этом репозитории я реализовал функции регистрации/активации/сброса пароля/смены пароля.
<br>
ДОПОЛНИТЕЛЬНО: В этом проекте пользователи могут авторизоваться через имя пользователя либо через емейл пользователя.
<br>
В основном это будет полезно при написании проекта с самого начала.
<br>

<b>ВНИМАНИЕ:</b>
<br>
В этом приложении я не прописывал css стили, отображение не имеет css стилизации, так как для каждого проекта стилизация будет индивидуальной. 
Css стили Вы должны будете настроить сами, так, как Вам необходимо.
<br>
<br>
        В папке "templates/base" Вы найдете файл base.html, который описывает базовый шаблон  приложения.
А в папке "templates/accounts" Вы найдете html файлы для отображения функций регистрации/ активации/сброса пароля/изменения пароля и др.
<br>
В этих файлах Вы можете кастомизировать отображение информации путем добавления/изменения css стилей
<br>
<br>
<b>Как настроить?</b>
<br>
Для начала клонируйте этот репозиторий.
<br>
Потом перейдите в папку с проектом (например - "cd django_accounts_email"). Создайте виртуально окружение, например - "pip -m venv venv".
<br>
Перейдите в папку с виртуальным окружением, в моем примере это - "cd venv".
<br>
Затем в папку Scripts и активируйте виртуальную среду.
<br>
Вернитесь в корневую папку проекта, перейдите в папку "core" (cd core) и выполните команду "pip install -r requirments.txt".
<br>
Таким образом Вы установили все необходимые зависимости.
Теперь осталось сделать миграции, применить их.
<br>
В коце концов в файле "settings.py" пропишите Ваши данные емейл сервиса, который вы будете использовать для отправки писем - это поля EMAIL_HOST, EMAIL_HOST_PASSWORD,
EMAIL_HOST_USER.
<br>
ГОТОВО! У вас есть базовый функционал приложения для работы с аккаунтами пользователей.
<br>
<b>ВНИМАНИЕ:</b>
Возможно Вам понадобится внести некоторые изменения в код, чтобы приложение работало так, КАК ХОТИТЕ ВЫ.
<br>
<br>
<br>
<b>
Прошу отнестись с пониманием, так как я не профессиональный разработчик django. Просто я считаю что это может быть полезно другим начинающим разработчикам, и в частности мне. Я рад любой обоснованной критике и замечаниям. Мне есть чему учиться, это бесспорно!
</b>
<br>
<br>
<br>
<b>Why do you need it?</b>
<br>
If you want to develop an application in which the user must confirm the email, 
as well as implement basic functions of the user's account, such as registration / activation of an account / reset of a password 
and similar, you do not need to write the same code every time that implements this functions. 
Just copy this repository and you will receive an application with the BASIC necessary functionality.
Also in this repository I implemented registration / activation / password reset / password change functions.
<br>
ADDITIONAL: In this project, users can log in through their username or through the user's email.
<br>
This will mostly be helpful when writing a project from the beginning.

<br>
<br>
<b>ATTENTION:</b>
<br>
In this application, I did not write css styles, the display does not have css styling, since the styling will be individual for each project. 
You will have to customize the css styles yourself, as you need.
<br>
<br>
In the "templates / base" folder, you will find a base.html file that describes the base application template.
And in the folder "templates / accounts" you will find html files for displaying the functions of registration / activation / password reset / password change, etc.
<br>
In these files, you can customize the display of information by adding / changing css styles
<br>
<br>
<b>How to setup?</b>
<br>
First, clone this repository.
<br>
Then go to the folder with the project (for example - "cd django_accounts_email"). Create a virtual environment, for example "pip -m venv venv".
<br>
Go to the folder with the virtual environment, in my example it is "cd venv".
<br>
Then go to the Scripts folder and activate the virtual environment. Go back to the root of the project, go to the "core" folder (cd core) and run the command "pip install -r requirments.txt".
<br>
This has installed all the required dependencies.
Now it remains to make migrations, apply them.
<br>
Finally, in the file "settings.py" write your data for the email service that you will use to send emails, these are the fields EMAIL_HOST, EMAIL_HOST_PASSWORD,
EMAIL_HOST_USER.
<br>
DONE! You have the basic functionality of the application for working with user accounts.
<br>
<b>ATTENTION:</b>
You may need to make some changes to the code in order for the application to work the way YOU WANT.
<br>
<br>
<br>
<b>
Please be understanding as I am not a professional django developer. I just think that it can be useful to other beginner developers and me too. I am glad to any reasonable criticism and remarks. I have a lot to learn, this is undeniable!
</b>
