# Практика 4

## Задача 1

```
git commit -am "commit on master 1"
git commit -am "commit on master 2"
git checkout -b first HEAD~1
git commit -am "commit on first 1"
git commit -am "commit on first 2"
git checkout master
git commit -am "commit on master 3"
git commit -am "commit on master 4"
git checkout -b second HEAD~3
git commit -am "commit on second 1"
git commit -am "commit on second 2"
git checkout master
git merge first
git checkout second
git rebase master
git checkout master
git merge second
git checkout HEAD~6
```

![image](https://github.com/mint1524/confUpr/blob/main/prak4/pic4.1.png)

## Задача 2

```
(base) min7t@Dmitrys-MacBook-Air ~ % git init
Reinitialized existing Git repository in /Users/min7t/.git/
(base) min7t@Dmitrys-MacBook-Air ~ % git config user.name "Coder 1"
(base) min7t@Dmitrys-MacBook-Air ~ % git config user.email "coder1@corp.com"
(base) min7t@Dmitrys-MacBook-Air ~ % echo "print('Hello, World!')" > prog.py
(base) min7t@Dmitrys-MacBook-Air ~ % python3 prog.py
Hello, World!
(base) min7t@Dmitrys-MacBook-Air ~ % git add prog.py
(base) min7t@Dmitrys-MacBook-Air ~ % git status
warning: could not open directory '.Trash/': Operation not permitted
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   prog.py
(base) min7t@Dmitrys-MacBook-Air ~ % git commit -m "Add prog.py file"

[main 3a86b4d] Add prog.py file
 1 file changed, 1 insertion(+), 1 deletion(-)
```

## Задача 3

```
(base) min7t@Dmitrys-MacBook-Air ~ % cd   
(base) min7t@Dmitrys-MacBook-Air ~ % mkdir project
(base) min7t@Dmitrys-MacBook-Air ~ % cd project
(base) min7t@Dmitrys-MacBook-Air project % git init
Initialized empty Git repository in /Users/min7t/project/.git/
(base) min7t@Dmitrys-MacBook-Air project % echo "print('Hello World')" > prog.py
(base) min7t@Dmitrys-MacBook-Air project % git config user.name "Coder1"
(base) min7t@Dmitrys-MacBook-Air project % git config user.email "coder1@test.com"
(base) min7t@Dmitrys-MacBook-Air project % git add prog.py
(base) min7t@Dmitrys-MacBook-Air project % git commit -m "Added prog.py"
[main (root-commit) 5e71554] Added prog.py
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
(base) min7t@Dmitrys-MacBook-Air project % cd
(base) min7t@Dmitrys-MacBook-Air ~ % git clone --bare project server.git
Cloning into bare repository 'server.git'...
done.
(base) min7t@Dmitrys-MacBook-Air ~ % cd project
(base) min7t@Dmitrys-MacBook-Air project % git remote add server ~/server.git
(base) min7t@Dmitrys-MacBook-Air project % echo "print('Hello again')" >> prog.py
(base) min7t@Dmitrys-MacBook-Air project % git add prog.py
(base) min7t@Dmitrys-MacBook-Air project % git commit -m "Updated prog.py"
[main 38bfe14] Updated prog.py
 1 file changed, 1 insertion(+)
(base) min7t@Dmitrys-MacBook-Air project % git push server main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 270 bytes | 270.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /Users/min7t/server.git
   5e71554..38bfe14  main -> main
(base) min7t@Dmitrys-MacBook-Air project % cd
(base) min7t@Dmitrys-MacBook-Air ~ % git clone server.git project2
Cloning into 'project2'...
done.
(base) min7t@Dmitrys-MacBook-Air ~ % cd project2
(base) min7t@Dmitrys-MacBook-Air project2 % git config user.name "Coder2"
(base) min7t@Dmitrys-MacBook-Air project2 % git config user.email "coder2@test.com"
(base) min7t@Dmitrys-MacBook-Air project2 % echo "Base program" > readme.md
(base) min7t@Dmitrys-MacBook-Air project2 % git add readme.md
(base) min7t@Dmitrys-MacBook-Air project2 % git commit -m "Added readme.md"
[main 5297cc7] Added readme.md
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md
(base) min7t@Dmitrys-MacBook-Air project2 % git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 280 bytes | 280.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /Users/min7t/server.git
   38bfe14..5297cc7  main -> main
(base) min7t@Dmitrys-MacBook-Air project2 % cd
(base) min7t@Dmitrys-MacBook-Air ~ % cd project
(base) min7t@Dmitrys-MacBook-Air project % git pull server main
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 260 bytes | 260.00 KiB/s, done.
From /Users/min7t/server
 * branch            main       -> FETCH_HEAD
   38bfe14..5297cc7  main       -> server/main
Updating 38bfe14..5297cc7
Fast-forward
 readme.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 readme.md
(base) min7t@Dmitrys-MacBook-Air project % echo "Coder1's program" >> readme.md
(base) min7t@Dmitrys-MacBook-Air project % git add readme.md
(base) min7t@Dmitrys-MacBook-Air project % git commit -m "Added Coder1's rights in readme.md"
[main 5815feb] Added Coder1's rights in readme.md
 1 file changed, 1 insertion(+)
(base) min7t@Dmitrys-MacBook-Air project % cd ../project2 
(base) min7t@Dmitrys-MacBook-Air project2 % echo "Coder2's program" > readme.md
(base) min7t@Dmitrys-MacBook-Air project2 % git add readme.md
(base) min7t@Dmitrys-MacBook-Air project2 % git commit -m "Added Coder2's rights in readme.md"
[main f616fac] Added Coder2's rights in readme.md
 1 file changed, 1 insertion(+), 1 deletion(-)
(base) min7t@Dmitrys-MacBook-Air project2 % git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 298 bytes | 298.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /Users/min7t/server.git
   5297cc7..f616fac  main -> main
(base) min7t@Dmitrys-MacBook-Air project2 % git pull origin main
From /Users/min7t/server
 * branch            main       -> FETCH_HEAD
Already up to date.
(base) min7t@Dmitrys-MacBook-Air project2 % git log
commit f616facb24f493b6cb730669481ee9a3420fb805 (HEAD -> main, origin/main, origin/HEAD)
Author: Coder2 <coder2@test.com>
Date:   Mon Nov 11 03:31:41 2024 +0300

    Added Coder2's rights in readme.md

commit 5297cc73210c8800a30de8a0d6d06f428b4b1c82
Author: Coder2 <coder2@test.com>
Date:   Mon Nov 11 03:27:30 2024 +0300

    Added readme.md

commit 38bfe14c975be89a6773a9cbd788d280cb136122
Author: Coder1 <coder1@test.com>
Date:   Mon Nov 11 03:24:56 2024 +0300

    Updated prog.py

commit 5e71554c2c8cc73a92f6504b9f4588a746362fdd
Author: Coder1 <coder1@test.com>
Date:   Mon Nov 11 03:22:49 2024 +0300

    Added prog.py
:
```

## Задача 4

```
import subprocess

def list_git_objects():
    objects = subprocess.run(['git', 'rev-list', '--objects', '--all'], text=True, capture_output=True).stdout.splitlines()
    
    for obj in objects:
        obj_id = obj.split()[0]
        content = subprocess.run(['git', 'cat-file', '-p', obj_id], text=True, capture_output=True).stdout
        print(f"Object {obj_id}:\n{content}\n{'-'*40}")

list_git_objects()
```

![image](https://github.com/mint1524/confUpr/blob/main/prak4/pic4.2.png)
