// xlsl to csv 출처 : https://github.com/SheetJS/js-xlsx/issues/214
function excelExport(event) {
  excelExportCommon(event, handleExcelDataAll);
}
function excelExportCommon(event, callback) {
  var input = event.target;
  var reader = new FileReader();
  reader.onload = function () {
    var fileData = reader.result;
    var wb = XLSX.read(fileData, { type: "binary" });
    var sheetNameList = wb.SheetNames; // 시트 이름 목록 가져오기
    var firstSheetName = sheetNameList[0]; // 첫번째 시트명
    var firstSheet = wb.Sheets[firstSheetName]; // 첫번째 시트
    callback(firstSheet);
  };
  reader.readAsBinaryString(input.files[0]);
}
function handleExcelDataAll(sheet) {
  handleExcelDataCsv(sheet); // csv 형태
}
function handleExcelDataCsv(sheet) {
  //$("#displayExcelCsv").html(XLSX.utils.sheet_to_csv(sheet));
  let split_with_enter = XLSX.utils.sheet_to_csv(sheet).split("\n");
  let subject_list = [];
  for (let i = 2; i < split_with_enter.length; i = i + 2) {
    subject_list.push(split_with_enter[i]);
  }
  for (let i in subject_list) {
    subject_list[i] = subject_list[i].split(",");
  }
  console.log(subject_list);
  localStorage.setItem("subject_list", JSON.stringify(subject_list));
}

function submit_form() {
  let Student_ID = [];
  Student_ID.push($("#ID_input").val());
  localStorage.setItem("subject_list", JSON.stringify(subject_list));
  localStorage.setItem("student_ID", JSON.stringify(Student_ID));
}
