CREATE DATABASE CustomerData2;
USE CustomerData2;

CREATE TABLE CustomerData2.dbo(WarehouseID  varchar(30) not null, Consignment_in_Date  VARCHAR(30) NOT NULL,Consignment_out_Date  VARCHAR(30) NOT NULL,Total_Storage_Cost  VARCHAR(30) NOT NULL, ConsignmentID varchar(30) not null);
Insert into CustomerData2.dbo (WarehouseID,ConsignmentID,Consignment_in_Date,Consignment_out_Date,Total_Storage_Cost)
            Select 'W1','C100230','13-06-20','19-06-20','2100' UNION ALL
            Select 'W2','C100231', '01-07-20','11-07-20','4000' UNION ALL
            Select 'W3', 'C100232','14-07-20','21-07-20' ,'3000' UNION ALL
            Select 'W4','C100233','25-07-20','31-07-20','5000' UNION ALL
           
Select * from CustomerData2.dbo;



