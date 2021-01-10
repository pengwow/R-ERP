import request from '@/utils/request'

const ordersApi = {
  UploadReport: '/orders/upload_report'

}

export function uploadReport (parameter) {
    return request({
      url: ordersApi.UploadReport,
      method: 'post',
      data: parameter
    })
  }
