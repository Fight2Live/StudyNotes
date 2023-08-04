# 装饰器介绍

```java
@id
@@unique(fields: [firstName, lastName], name: "fullname")
```

# 模型查询

- findUnique
  
  - 使用唯一条件来获取单个数据记录，如根据id查询
  
  - 支持关键字：where, select, include
  
  - ```javascript
    const result = await prisma.user.findUnique({
      where: {
        email: 'alice@prisma.io',
      },
    })
    ```

- findFirst
  
  - 返回第一个匹配条件的记录
  
  - 支持关键字：select, include, rejectOnNotFound, where, orderBy, cursor, take, skip, distinct
  
  - ```javascript
    // 获取 title 字段以 A test 开头的第一个 Post 记录，并反转列表（take）
    async function main() {
      const a = await prisma.post.create({
        data: {
          title: 'A test 1',
        },
      })
    
      const b = await prisma.post.create({
        data: {
          title: 'A test 2',
        },
      })
    
      const c = await prisma.post.findFirst({
        where: {
          title: {
            startsWith: 'A test',
          },
        },
        orderBy: {
          title: 'asc',
        },
        take: -1, // 反转列表
      })
    }
    ```

- findMany
  
  - 返回多条记录
  
  - 支持关键字：select, include, where, orderBy, cursor, take, skip, distinct
  
  - ```javascript
    const user = await prisma.user.findMany({
      where: { name: 'Alice' },
    })
    ```

- create
  
  - 创建一条新的数据库记录
  
  - 支持关键字：data, select, include
  
  - Prisma Client 当前不支持在数据库级别批量插入，可手动通过循环实现
  
  - ```javascript
    const user = await prisma.user.create({
      data: { email: 'alice@prisma.io' },
    })
    ```

- update
  
  - 更新数据
  
  - 支持关键字：data, where, select, include
  
  - ```javascript
    const user = await prisma.user.update({
      where: { id: 1 },
      data: { email: 'alice@prisma.io' },
    })
    ```

- upsert
  
  - 更新现有、或创建新的数据库记录
  
  - 支持关键字：create, update, where, select, include
  
  - ```javascript
    // 更新（如果存在）或创建一条 email 为 alice@prisma.io 的 User 记录
    const user = await prisma.user.upsert({
      where: { id: 1 },
      update: { email: 'alice@prisma.io' },
      create: { email: 'alice@prisma.io' },
    })
    ```

- delete
  
  - 删除现有的数据库记录
  
  - 只支持根据id，或者unique属性进行删除
  
  - 支持关键字：where, select, include
  
  - ```javascript
    const user = await prisma.user.delete({
      where: { id: 1 },
    })
    ```

- deleteMany
  
  - 删除多条记录，可根据筛选条件批量删除
  
  - 支持关键字：where
  
  - ```javascript
    // 删除所有 name 为 Alice 的 User 记录
    const deletedUserCount = await prisma.user.deleteMany({
      where: { name: 'Alice' },
    })
    
    // 删除所有User
    const deletedUserCount = await prisma.user.deleteMany({})
    ```

- createMany
  
  - 在一个事务中创建多个记录，并返回成功插入数
  
  - 支持关键字：data, skipDuplicates
  
  - ```javascript
    const users = await prisma.user.createMany({
      data: [
        { name: 'Sonali', email: 'sonali@prisma.io' },
        { name: 'Alex', email: 'alex@prisma.io' },
      ],
    })
    ```

- updateMany
  
  - 更新一批已存在的数据库记录，并返回更新的记录数
  
  - 支持关键字：data, where
  
  - ```javascript
    const updatedUserCount = await prisma.user.updateMany({
      where: { name: 'Alice' },
      data: { name: 'ALICE' },
    })
    ```

- count
  
  - 返回符合条件的数据计数
  
  - 支持关键字：where, cursor, skip, take, orderBy, distinct, select
  
  - ```javascript
    // 查询所有记录总数、查询name字段非空的总数，查询city字段非空的总数
    const c = await prisma.user.count({
      select: {
        _all: true,
        city: true,
        name: true,
      },
    })
    ```

- aggregate
  
  - 支持关键字：where, orderBy, cursor, skip, take, distinct, _count, _avg, _sum, _min, _ max
  
  - ```javascript
    // 返回所有User记录的profileViews的_min、_max和_count
    const minMaxAge = await prisma.user.aggregata({
        _count: {
        _all: true,
    },
        _max: {
        profileViews: true,
    },
        _min: {
        profileViews: true,
    }
    })
    
    // return : {
    //  _count: { _all: 29 },
    //  _max: { profileViews: 90 },
    //  _min: { profileViews: 0 }
    //}
    ```

- groupBy
  
  - 聚合操作
  
  - 支持关键字：where, orderBy, by, having, skip, take, _count, _avg, _sum, _min, _max
  
  - ```javascript
    // 按平均 profileViews 大于 200 的 country/city 分组，并返回每组 profileViews 的 _sum
    const groupUsers = await prisma.user.groupBy({
      by: ['country', 'city'],
      _count: {
        _all: true,
        city: true,
      },
      _sum: {
        profileViews: true,
      },
      orderBy: {
        country: 'desc',
      },
      having: {
        profileViews: {
          _avg: {
            gt: 200,
          },
        },
      },
    })
    ```

# 模型查询选项

| 关键字名称            |     | 描述                        |     |
| ---------------- | --- | ------------------------- | --- |
| where            |     | 可以通过任何属性来过滤列表             |     |
| select           |     | 指定返回的对象中要包含的属性，默认全返回      |     |
| include          |     | 指定返回的对象要加载的关系对象           |     |
| distinct         |     | 按特定字段来过滤重复行               |     |
| cursor           |     | 指定列表的位置，通常指定一个 id 或另一个唯一值 |     |
| orderBy          |     | 允许按照任何属性进行排序              |     |
| skip             |     | 指定应跳过聊表中返回的对象数量           |     |
| take             |     | 指定应在列表中返回多少个对象。若为负值则会反转列表 |     |
| skipDuplicates   |     | 是否插入具有唯一字段、或已存在ID的记录      |     |
| _count           |     | 返回匹配记录或非空字段的数量            |     |
| _avg             |     | 返回指定字段的所有值的平均值            |     |
| _sum             |     | 返回指定字段值的总和                |     |
| _min             |     | 返回指定字段的最小可用之              |     |
| _max             |     | 返回指定字段的最大可用之              |     |
| rejectOnNotFound |     |                           |     |

# 迁移

> [Prisma Migrate](https://www.prisma.io/docs/concepts/components/prisma-migrate)
> 
> [CLI Reference migrate](https://www.prisma.io/docs/reference/api-reference/command-reference#migrate-dev)

        为了将其他开发人员的数据库机构同步至本地，可以通过`prisma generate`进行数据库迁移。它能够生成本地的一个`.sql`数据库结构文件，并一起通过git进行版本管理。

        需要注意的是，它的主要目的是管理数据库结构的变化，并不会带着数据一起。

## 相关命令

```shell
npx prisma db pull
npx prisma db push

# 此命令删除并重新创建数据库，或通过删除所有数据、表、索引和其他来进行重置
npx prisma migrate reset

# 将schema.prisma中的模型迁移至数据库，若冲突会以schema中的为准，reset数据库
npx prisma migrate dev
## dev的一些参数
--name %optionName%    # 命名此次迁移
--create-only          # 只生成迁移文件，不自动执行，可人为进行修改，后续需要再次执行dev命令使其生效

# 命令用于将更改部署到暂存、测试和生产环境，它只运行迁移文件。
# 它不会使用 Prisma 架构文件来获取模型。
npx prisma migrate deploy

# 可将迁移标记为以应用，或回滚至目标版本
npx prisma migrate resolve
--applied %migrateName%   # 将migrateName标为已应用，执行dev时会跳过改迁移
--rolled-back %migrateName%  # 回滚至migrateName版本的迁移
```

## 操作

        执行以下命令后，会根据`schema.prisma`文件，与数据库进行比对后，生成`TimeStamp_%option_name%.sql`文件

```shell
yarn prisma migrate dev --name %option_name%
```

        如果是第一次执行，会进行

> 需要注意的是，Prisma不支持一些数据库特性的迁移，包括但不限于：
> 
> - 存储过程
> 
> - 触发器
> 
> - 视图
> 
> - 部分索引
> 
> - 字段修改
> 
> 要在数据库中添加一个不支持的特性, 必须执行迁移前在[自定义迁移](https://prisma.yoga/guides/database/developing-with-prisma-migrate/customizing-migrations/)中包含该特性。

### 字段修改

默认情况下，重命名schema中的一个字段会导致:

- `CREATE` 一新的列 (例如, `fullname`)
- `DROP` 现有列 (for example, `name`) 和该列中的数据

要真正**重命名**一个字段，且在生产中运行迁移时避免数据丢失，需要在将迁移 SQL 应用到数据库之前修改生成的迁移 SQL 语句。考虑下面的 schema 片段 - `biograpy`字段是拼写错误的。

```python
model Profile {  
    id       Int    @id @default(autoincrement())  
    biograpy String  # 需要更改
    userId   Int  
    user     User   @relation(fields: [userId], references: [id])
}
```

1. 重命名 `biograpy` 字段为 `biography`:

```python
model Profile {  
    id       Int    @id @default(autoincrement())  
    biography String  # 修改后
    userId   Int  
    user     User   @relation(fields: [userId], references: [id])
}
```

2. 运行命令，表示仅生成迁移文件，但不执行

```shell
npx prisma migrate dev --name rename-migration --create-only
```

3. 将生成的`.sql`文件中的语句由`DROP COLUMN, ADD COLUMN` ，更改为`RENAME TO`

```sql
ALTER TABLE "Profile" RENAME COLUMN "biograpy" TO "biography"
```

4. 保存与应用

```shell
npx prisma migrate dev
```

5. 如果同时还修改了字段类型，在第四步结束后，会自动再生成一个`.sql`迁移文件，并提示输入`migrate name`

![](C:\Users\30935\AppData\Roaming\marktext\images\2023-07-31-12-01-21-image.png)

## 回滚

        基于prisma工具的功能，有两种回滚方式，一种是向上迁移发生异常时需要回滚，另一种是已经向上迁移成功后因其他原因需要回滚。

### 异常回滚

        在`dev \ deploy`期间，**如发生错误**，可通过执行`npx prisma db execute --file down.sql`来将数据库结构回退至最近的版本。

        但需要在`dev \ deploy`前，先执行以下语句来生成down.sql文件。

```shell
npx prisma migrate diff \
    --from-schema-datamodel .\prisma\schema.prisma \
    --to-schema-datasource .\prisma\schema.prisma \
    --script ">down.sql"
```

`migrate diff`的原理是比较`from`中的数据结构，与`to`中的数据结构是否相同。

然后执行`npx prisma db execute --file down.sql`手动还原结构。并还需要执行`npx prisma migrate resolv --rolled-back 20230802024446_diff_3`来将发生错误的迁移标为已回滚，只要这样才能当错误解决完后继续通过`dev \ deploy`命令来继续迁移。

### 正常回滚

        如果在`dev \ deploy`期间没发生错误，已经成功向上迁移，则原先生成的`down.sql`文件其实就不会有应用场景了。这时如果像上面一样操作，就会导致数据库结构与项目模型不一致，在进行`dev \ deploy`时会要求**重置数据库**。

        所以如果向上迁移成功，而我们有需要将结构还原，那么最好的就是去更改`schema.prisma`中的结构，重新生成一个新的向上迁移文件，已进为退。

**如果需要回滚至特定版本，可以采取以下方法**：

1. （推荐）直接更改`schema.prisma`文件，创建新的迁移，以进为退。

2. 清空数据库中的`_prisma_migrations表`，并将文件夹`./prisma/migrations/`下的文件夹删除至想要回退到的版本，然后重新执行迁移命令。（但该操作会导致其他开发人员本地的migrate不匹配，数据库结构异常，同时还有面临清空数据的风险）

3. 进行新迁移前，先通过`migrate diff`命令生成向下迁移的sql文件，当`dev \ deploy`发生异常需要回退时，执行
   
   ```shell
   # 生成向下迁移文件
   npx prisma migrate diff --from-schema-datamodel .\prisma\schema.prisma --to-schema-datasource .\prisma\schema.prisma --script ">down.sql"
   
   # 执行向下迁移文件
   npx prisma db execute --file ./down.sql --schema prisma/schema.prisma
   
   # 标记异常迁移
   npx prisma migrate resolve --rolled-back add_profile
   ```





## 常见问题

### 执行`prisma db execute --file down.sql`时，报编码错误：

```log
Error: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '��-' at line 1
```

**解决方式1**：

        可能是由于在生成`down.sql`文件时，命令异常导致的编码问题，如果是在Windows平台下执行的`diff`命令，确保`--script ">down.sql"`后面有双引号括起来。

**解决方式2**：

        如果是在本地执行发生这个异常，也可以通过`navicat`等数据库工具来执行该文件

### 迁移异常 - 结构与历史不一致

        这个是数据库中的结构，与项目的迁移历史不一致导致的，比如数据库中存在表A，但创建表A的迁移还没执行，这时候就会出现以下提示：

```log
- The migration `20230802024446_diff_3` failed.
- Drift detected: Your database schema is not in sync with your migration history.

The following is a summary of the differences between the expected database schema given your migrations files, and the actual schema of the database.

It should be understood as the set of changes to get from the expected schema to the actual schema.

[+] Added tables
  - test_diff_3
  - test_diff_4


? We need to reset the MySQL database "test_generate" at "127.0.0.1:3306".
Do you want to continue? All data will be lost. » (y/N)
```

**解决方式1**

        将发生异常的迁移标记为已解决，然后继续执行

```shell
npx prisma migrate resolv --applied 20230802024446_diff_3
npx prisma migrate dev
```

### 迁移异常 - 新结构已存在

        这是由于准备要执行的迁移文件内容已经在数据库中存在了，如下报错信息所示，提示表`test_diff_3`已存在

```log
Applying migration `20230802024446_diff_3`
Error: P3018

A migration failed to apply. New migrations cannot be applied before the error is recovered from. Read more about how to resolve migration issues in a production database: https://pris.ly/d/migrate-resolve

Migration name: 20230802024446_diff_3

Database error code: 1050

Database error:
Table 'test_diff_3' already exists

Please check the query number 1 from the migration file.
```

**解决方式1**

        将该迁移记为已解决，然后继续执行

```shell
npx prisma migrate resolv --applied 20230802024446_diff_3
npx prisma migrate deploy
```

**解决方式2**

        如果数据库中的新结构还不存在数据，可以手动去删除新结构，然后将迁移标为已回滚，再继续执行

```shell
npx prisma migrate resolv --rolled-back 20230802024446_diff_3
npx prisma migrate deploy
```

### 迁移异常 - 发现未解决的迁移错误

        这是由于上一次执行时发生错误，没有完全解决导致的。当我们解决完错误后，还需要

使用命令`migrate resolv --rolled-bake`将迁移记录回滚，然后才能继续执行

```log
Error: P3009

migrate found failed migrations in the target database, new migrations will not be applied. Read more about how to resolve migration issues in a production database: https://pris.ly/d/migrate-resolve
The `20230802055625_diff_4` migration started at 2023-08-02 09:10:42.974 UTC failed
```

**解决方式**

```shell
npx prisma migrate resolv --rolled-back 20230802055625_diff_4
npx prisma migrate deploy
```
