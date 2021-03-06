//
// SymbolInfo.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct SymbolInfo: Codable {

    public var name: String?
    public var baseCurrency: String?
    public var quoteCurrency: String?
    public var priceScale: Double?
    public var priceFilter: Any?
    public var lotSizeFilter: Any?

    public init(name: String?, baseCurrency: String?, quoteCurrency: String?, priceScale: Double?, priceFilter: Any?, lotSizeFilter: Any?) {
        self.name = name
        self.baseCurrency = baseCurrency
        self.quoteCurrency = quoteCurrency
        self.priceScale = priceScale
        self.priceFilter = priceFilter
        self.lotSizeFilter = lotSizeFilter
    }

    public enum CodingKeys: String, CodingKey { 
        case name
        case baseCurrency = "base_currency"
        case quoteCurrency = "quote_currency"
        case priceScale = "price_scale"
        case priceFilter = "price_filter"
        case lotSizeFilter = "lot_size_filter"
    }


}

