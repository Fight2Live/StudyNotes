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