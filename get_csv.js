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
  let csv_odd = [];
  for (let i = 2; i < split_with_enter.length; i = i + 2) {
    csv_odd.push(split_with_enter[i]);
  }
  console.log(csv_odd);
  document.getElementById("csv_result").innerHTML = csv_odd.join("<br>");
}

function submit_form() {
  $("#id_result").text($("#ID_input").val());
}
