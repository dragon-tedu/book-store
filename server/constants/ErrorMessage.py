errorMessage = {
    # valid input KPI-0000xxx
    "SAMPLE_ID_NOT_FOUND": "KPI-0000001",
}

errorMessageVN = {
    "SAMPLE_ID_NOT_FOUND": "Not fond sample id",
    "PARAM_TYPE_INCORRECT": "Param type incorrect value",
    "PARAM_ISACTIVED_INCORRECT": "Param isActived incorrect value",
    "PARAM_TYPEOFAUDIOTEST_INCORRECT": " Param typeOfAudioTest incorrect value",
    "PARAM_SCORE_INCORRECT": "Param score incorrect value",
    "PARAM_OPERATOR_INCORRECT": "Param operator incorrect value",
    "PARAM_KPI_INCORRECT": "Param kpi incorrect value",
    "PARAM_MAXSIZE_INVALID": "Param maxSize incorrect value: only from 1 to 1000",
    "PARAM_PAGE_INVALID": "Param page incorrect value: only from 1",
    "PARAM_NAME_INCORRECT": "Param name required",
    "PARAM_ERROR_TYPE_INCORRECT": "Param errorType must only one in greeting, qualification, created_crm_ticket, "
    "attitude",
}

errorStatus = {
    "SAMPLE_ID_NOT_FOUND": 404,
    "PARAM_TYPE_INCORRECT": 400,
    "PARAM_ISACTIVED_INCORRECT": 400,
    "PARAM_TYPEOFAUDIOTEST_INCORRECT": 400,
    "PARAM_SCORE_INCORRECT": 400,
    "PARAM_OPERATOR_INCORRECT": 400,
    "PARAM_KPI_INCORRECT": 400,
    "PARAM_MAXSIZE_INVALID": 400,
    "PARAM_NAME_INCORRECT": 400,
    "PARAM_ERROR_TYPE_INCORRECT": 400,
    # criteria error KPI-0001xxx
    "CRITERIA_NOT_FOUND": 500,
    "CRITERIA_DETAIL_NOT_FOUND": 500,
    "TYPE_CRITERIA_NOT_SUPPORT": 400,
    "PARAM_PAGE_INVALID": 400,
    # kpi error KPI-0002xxx
    "KPI_NOT_FOUND": 500,
    # kpi group error KPI-0003xxx
    "KPI_GROUP_NOT_FOUND": 500,
    # kpi config error KPI-0004xxx
    "KPI_CONFIG_NOT_FOUND": 500,
    "JWT_EXPIRED": 403,
    "KPI_CONFIG_IMPORT_IS_FAILED": 400,
    "KPI_CONFIG_IMPORT_WRONG_FORMAT": 400,
}
