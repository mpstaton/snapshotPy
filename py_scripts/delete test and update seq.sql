delete from collecteddatapoints where id>=4;
delete from contactcards where id>=9;
delete from interactionmaterials where id>=3;
delete from interactions where id>=3;
delete from organizations where id>=98;
delete from persons where id>=19;
delete from variabledocumentation where id>=4;

alter sequence collecteddatapoints_id_seq restart 4;
alter sequence contactcards_id_seq restart 9;
alter sequence interactionmaterials_id_seq restart 3;
alter sequence interactions_id_seq restart 3;
alter sequence organizations_id_seq restart 98;
alter sequence persons_id_seq restart 19;
alter sequence variabledocumentation_id_seq restart 4;