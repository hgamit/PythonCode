--Exhibit F - Ragular Pay
SELECT SiteCounty,JobSkill,BaseRatePerHour,FringeBenefit,(BaseRatePerHour+FringeBenefit) AS Total, SUM(RegHoursWorked) AS TotalHours, (BaseRatePerHour+FringeBenefit)*SUM(RegHoursWorked) AS Gross
FROM TIMESHEET 
JOIN PROJECT ON TIMESHEET.ProjectID=PROJECT.ProjectID
JOIN PAYRATE ON PAYRATE.PayrateID=TIMESHEET.PayrateID
JOIN EMPLOYEE ON TIMESHEET.EmployeeID=EMPLOYEE.EmployeeID
WHERE TIMESHEET.EmployeeID=90922
GROUP BY SiteCounty, JobSkill,BaseRatePerHour,FringeBenefit;

--Exhibit F - Overtime Pay
SELECT SiteCounty,JobSkill,BaseRatePerHour,FringeBenefit,(Overtime*BaseRatePerHour+FringeBenefit) AS Total, SUM(OvertimeHoursWorked) AS TotalHours, (Overtime*BaseRatePerHour+FringeBenefit)*SUM(OvertimeHoursWorked) AS Gross
FROM TIMESHEET 
JOIN PROJECT ON TIMESHEET.ProjectID=PROJECT.ProjectID
JOIN PAYRATE ON PAYRATE.PayrateID=TIMESHEET.PayrateID
JOIN EMPLOYEE ON TIMESHEET.EmployeeID=EMPLOYEE.EmployeeID
WHERE TIMESHEET.EmployeeID=90922
GROUP BY SiteCounty, JobSkill,BaseRatePerHour,FringeBenefit,Overtime;
