function check_remaining_credits (classes, curriculum) {
    let length = curriculum.length
    let lectures_credits_taken = new Array(length)

    for (let i=0; i<classes.length; i++) {
        for (let j=0; j<length; j++) {
            if ( Object.values(curriculum[i]).includes(classes[i]['name']) ) {
                lectures_credits_taken[i] += classes[i]['credit']
                break;
            }
        }
    }
    return lectures_credits_taken;
}

// data = "csv"
let data = []

let major_classes = []
let GE_classes = []

let total_classes_names = []

// let temp = [1,2,3]
// for (vari of temp) {
//     console.log(vari)
// }

for (row of odd_rows) {
    let lecture = {'name':row[4],'classification':row[5], 'credit':int(row[6]), 'grade':row[8]};
    total_classes_names.push(row[4])

    if (row[6] === 'P') {
        lecture['grade'] = 4.5; // needs to be fixed, don't count this into GPA
    }
    if (row[6] === 'F') {
        lecture['grade'] = 0.0;
    }
    if (lecture['classification'] === '전공') {
        major_classes.push(lecture);
    }
    if (lecture['classification'] === '교양') {
        GE_classes.push(lecture);
    }
}

let total_credits_major = 0;
let total_credits_GE = 0;

let GPA_major = 0.0;
let GPA_GE = 0.0;
let GPA_total = 0.0;

for (course of major_classes) {
    total_credits_major += course['credit'];
    GPA_major += course['credit'] * course['grade'];
}

for (course of GE_classes) {
    total_credits_GE += course['credit'];
    GPA_GE += course['credit'] * course['grade'];
}

GPA_total = (GPA_major + GPA_GE) / (total_credits_major + total_credits_GE);
GPA_major /= total_credits_major;
GPA_GE /= total_credits_GE

let experiment_credit = 0.0 // 실험실습.
let major_core_credit = 0.0 // 전공코어 (or 전공핵심).
let major_credit = 0.0 // 전공일반 (or 전공심화).

if (admission_year >= 2021) {
    experiment_credit = 6
    major_core_credit = 36
    major_credit = 21
    for (lecture of major_classes) {
        if (newSoft[0].includes(lecture['name'])) {
            major_core_credit -= lecture['credit']
        }
        if (newSoft[1].includes(lecture['name'])) {
            major_credit -= lecture['credit']
        }
        if (newSoft[2].includes(lecture['name'])) {
            experiment_credit -= lecture['credit']
        }
    }
}

if (admission_year < 2021) {
    experiment_credit = 14
    major_core_credit = 27
    major_credit = 24
    for (lecture of major_classes) {
        if (oldSoft[0].includes(lecture['name'])) {
            major_core_credit -= lecture['credit']
        }
        if (oldSoft[1].includes(lecture['name'])) {
            major_credit -= lecture['credit']
        }
        if (oldSoft[2].includes(lecture['name'])) {
            experiment_credit -= lecture['credit']
        }
    }
}

