# DBA_Airflow
ДОКУМЕНТАЦИЯ:

В качестве СУБД использовалась PostgreSQL.

В блоке SQL для каждого задания было использовано по одному решению.

Обьяснение выбора решений каждого задания.

1. 
- Производительность, LIMIT эффективно ограничивает количество возвращаемых строк.
- Запрос короткий и легко читаемый, что упрощает его поддержку и модификацию.

2.
 - Универсальность, гибкость в работе с данными. 
 - Поддержка старых версий SQL.

 3.
 - Обеспечение точного получения инфы, а также высокую эффективность.
 - Запрос учитывает все важные аспекты обработки данных.
 

 Блок Airflow:

- Сделал стандартную настройку Dag;
- Подключился к PostgreSQL;
- Создал новую таблицу для записи;
- Выполнение запроса и запись результатов;

