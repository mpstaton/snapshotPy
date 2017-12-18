delete from collecteddatapoints where id>=4;
delete from contactcards where id>=6;
delete from interactionmaterials where id>=3;
delete from interactions where id>=2;
delete from organizations where id>=98;
delete from persons where id>=16;
delete from variabledocumentation where id>=3;

alter sequence collecteddatapoints_id_seq restart 4;
alter sequence contactcards_id_seq restart 6;
alter sequence interactionmaterials_id_seq restart 3;
alter sequence interactions_id_seq restart 2;
alter sequence organizations_id_seq restart 98;
alter sequence persons_id_seq restart 16;
alter sequence variabledocumentation_id_seq restart 3;