import request from '@/utils/request'

const ordersApi = {
  UploadReport: '/orders/upload_report',
  GetOrderList: '/orders/list'

}

export function uploadReport (parameter) {
    return request({
      url: ordersApi.UploadReport,
      method: 'post',
      data: parameter
    })
  }

export function getOrderList (parameter) {
    return request({
      url: ordersApi.GetOrderList,
      method: 'get',
      params: parameter
    })
}
